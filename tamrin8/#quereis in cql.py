#quereis in cql
#soal1
 cqlsh>SELECT prediction,COUNT(*)FROM eshaghi.finaltablenumerictime GROUP BY prediction;

#soal2
 cqlsh>SELECT base,COUNT(*) FROM eshaghi.finaltablebase WHERE datetime>= 0 AND datetime < 604800 GROUP BY base ALLOW FILTERING;
cqlsh> SELECT base,COUNT(*) FROM eshaghi.finaltablebase WHERE datetime > 1728000 AND datetime < 2332800  GROUP BY base ALLOW FILTERING;
#soal3
SELECT prediction,COUNT(*) FROM eshaghi.finaltablenumerictime WHERE datetime >= 1728000 AND datetime < 2332800  GROUP BY prediction ALLOW FILTERING;