SELECT instrument_id,
	AVG(CASE WHEN sensor = 'S0' THEN ROUND(value,3) END) S0,
	AVG(CASE WHEN sensor = 'S1' THEN ROUND(value,3) END) S1,
	AVG(CASE WHEN sensor = 'S2' THEN ROUND(value,3) END) S2,
	AVG(CASE WHEN sensor = 'S3' THEN ROUND(value,3) END) S3,
	AVG(CASE WHEN sensor = 'S4' THEN ROUND(value,3) END) S4,
	AVG(CASE WHEN sensor = 'S5' THEN ROUND(value,3) END) S5,
	AVG(CASE WHEN sensor = 'S6' THEN ROUND(value,3) END) S6,
	AVG(CASE WHEN sensor = 'S7' THEN ROUND(value,3) END) S7,
	AVG(CASE WHEN sensor = 'S8' THEN ROUND(value,3) END) S8,
	AVG(CASE WHEN sensor = 'S9' THEN ROUND(value,3) END) S9,
	AVG(CASE WHEN sensor = 'S10' THEN ROUND(value,3) END) S10
FROM measurements GROUP BY instrument_id;
