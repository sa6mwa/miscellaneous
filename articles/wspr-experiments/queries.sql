-- These SQL statements are intended to be used with the database generated by
-- create-and-populate-database.sh

.mode column
.headers on


-- WSPR test 2021-03-16 on 80m comparing 3 types of antennas based on the same
-- 8m wire using 5 watts:
-- End-fed 8m wire with a 9:1 transformer coupled by an ATU (9to1wATU)
-- End-fed 8m wire with a 9:1 transformer terminated at the end of the
--   wire with a 500 ohm resistor, ground goes back to ground plug of
--   transformer (9to1w500ohm)
-- End-fed 8m wire with a 50 ohm dummy load where the 8m wire is connected
--   to the "hot" end of the dummy load, an "aperiodic" dumb antenna in a
--   parallel resistance configuration with a lot of loss. There were
--   no recorded spots using this antenna in this test, which is why it's
--   not in the statements below (see the 20m test the following day).

select wsprspots.qrz as qrz, count(wsprspots.snr) as spots,
  avg(wsprspots.snr) as snr9to1w500ohm,
  q9to1atu.avgsnr as snr9to1wATU,
  q9to1atu.avgsnr - avg(wsprspots.snr) as db_better_w_9to1wATU_abv_9to1w500ohm
  from wsprspots,
  (select qrz, avg(snr) as avgsnr from wsprspots
    where subset="unterminated9to1watu" and date(dt) = "2021-03-16"
    group by qrz) q9to1atu
  where q9to1atu.qrz = wsprspots.qrz
    and subset="9to1w500ohm2"
    and date(wsprspots.dt) = "2021-03-16"
  group by wsprspots.qrz having count(wsprspots.snr) > 1;


-- WSPR test 2021-03-17 on 20m comparing the same 3 type of antennas
-- as above, but this time with more power (20W) which produced a few
-- spots for the 50 ohm dummy load "antenna" (dummyload).

select wsprspots.qrz as qrz, count(wsprspots.snr) as spots,
  avg(wsprspots.snr) as snrdummyload,
  q500ohm.avgsnr as snr9to1w500ohm,
  q9to1atu.avgsnr as snr9to1wATU,
  q9to1atu.avgsnr - avg(wsprspots.snr) as db_better_w_9to1wATU_abv_dl,
  q500ohm.avgsnr - avg(wsprspots.snr) as db_better_w_9to1w500ohm_abv_dl,
  q9to1atu.avgsnr - q500ohm.avgsnr as db_better_w_9to1atu_abv_9to1w500ohm
  from wsprspots,
  (select qrz, avg(snr) as avgsnr from wsprspots
    where subset="9to1w500ohm" and date(dt) = "2021-03-17"
    group by qrz) q500ohm,
  (select qrz, avg(snr) as avgsnr from wsprspots
    where subset="unterminated9to1watu" and date(dt) = "2021-03-17"
    group by qrz) q9to1atu
  where q9to1atu.qrz = wsprspots.qrz and q500ohm.qrz = wsprspots.qrz
    and subset="dummyload50ohm8mwire"
    and date(wsprspots.dt) = "2021-03-17"
  group by wsprspots.qrz having count(wsprspots.snr) > 1;

select wsprspots.qrz as qrz, count(wsprspots.snr) as spots,
  avg(wsprspots.snr) as snr9to1w500ohm,
  q9to1atu.avgsnr as snr9to1wATU,
  q9to1atu.avgsnr - avg(wsprspots.snr) as db_better_w_ATU_abv_500ohm
  from wsprspots,
  (select qrz, avg(snr) as avgsnr from wsprspots
    where subset="unterminated9to1watu" and date(dt) = "2021-03-17"
    group by qrz) q9to1atu
  where q9to1atu.qrz = wsprspots.qrz
    and subset="9to1w500ohm"
    and date(wsprspots.dt) = "2021-03-17"
  group by wsprspots.qrz having count(wsprspots.snr) > 1;


