#!/usr/bin/env python
# coding: utf-8

# In[63]:


#assigining variables 

input_file = "c:/users/91734/Desktop/b.csv"
output_file = "c:/users/91734/Desktop/new1.avro"
# importing and creating spark session
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("CSV to Avro Conversion").config("spark.jars.packages","org.apache.spark:spark-avro_2.12:3.4.0").getOrCreate()

df = spark.read.format("csv").option("header", "True").load(input_file)

df.show()


# In[3]:


#schema optional
schema =  open(r'c:/users/91734/Desktop/data_schema.avsc', "r").read()
schema


# In[4]:


from pyspark.sql.avro.functions import from_avro, to_avro


# #diff writing modes and options
# ##### --- df.write \
#     .format("csv") \
#     .mode("overwrite") \
#     .option("header", "true") \
#     .option("delimiter", ",") \
#     .option("compression", "gzip") \
#     .partitionBy("Year", "Month") \
#     .save(output_path) --###

# In[44]:


#different modes : "append","overwrite","ignore","error","dynamic"
#writing dataframe to avro format
df.write.mode("append").format("avro").save(out_path)


# In[49]:


#reading avro file
spark.read.format("avro").load(output_file)

