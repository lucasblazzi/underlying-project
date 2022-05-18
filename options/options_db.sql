CREATE DATABASE IF NOT EXISTS db_underlying;
USE db_underlying;

CREATE EXTERNAL TABLE `tb_options_series`(
  `date` date,
  `company` string,
  `currency` string,
  `open_price` double,
  `max_price` double,
  `min_price` double,
  `average_price` double,
  `close_price` double,
  `transactions` double,
  `quantity` double,
  `volume` double,
  `exercise_price` double,
  `expiration_date` date,
  `isin_code` string,
  `type` string,
  `id` string,
  `name_underlying` string,
  `company_underlying` string,
  `close_price_underlying` double,
  `expiration_time` double,
  `option_value` double,
  `intrinsic_value` double,
  `time_value` double,
  `delta` double,
  `theta` double,
  `rho` double,
  `gamma` double,
  `vega` double,
  `hedge_ratio` double)
PARTITIONED BY (
  `name` string)
ROW FORMAT SERDE
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
STORED AS INPUTFORMAT
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://underlying-options-series/'
TBLPROPERTIES (
  'transient_lastDdlTime'='1652831396')

MSCK REPAIR TABLE `db_underlying`.`options_series`
