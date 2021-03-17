drop table if exists wsprspots;
create table wsprspots (
  wsprspotId integer primary key not null,
  dt datetime not null,
  subset varchar(64) not null,
  qrz varchar(16) not null,
  snr float not null,
  pwr float not null,
  km float not null
);
