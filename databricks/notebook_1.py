# Databricks notebook source
env = dbutils.widgets.get("env")

# COMMAND ----------

checkpoint_location = f'dbfs:/tmp/neilp/{env}/notebook_1/checkpoint'
write_location = f'dbfs:/tmp/neilp/{env}/notebook_1/data'

# COMMAND ----------

df = spark.readStream.format('cloudFiles') \
  .option('cloudFiles.format', 'json') \
  .option('cloudFiles.schemaHints', 'time timestamp, action string') \
  .option('cloudFiles.schemaLocation', checkpoint_location) \
  .load("dbfs:/databricks-datasets/structured-streaming/events")

# COMMAND ----------

df.writeStream.format('delta') \
  .option('checkpointLocation', checkpoint_location) \
  .trigger(once=True) \
  .start(write_location)
