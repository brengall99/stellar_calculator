SELECT 
  * 
FROM 
  (
    SELECT 
      id, tyc, gaia, hyg, hip, hd, hr, gl, -- ID's from individual datasets
      bayer, -- Bayer designation
      con AS constellation, 
      proper, -- Proper name if exists
      ra, dec, -- Right ascension and declination to determine position
      dist * 3.262 AS dist_ly, 
      x0, y0, z0,
      dist_src, -- Indicator for source for the distance
      mag, absmag, -- Apparent and absolute magnitude
      spect, ci -- Spectral type and color index

    FROM
      `stellar-calculator.stellar_dataset.stellar_data`
  ) AS subquery

  WHERE
    dist_ly BETWEEN 0 AND 6200 -- Limit maximum 'time' to 6200 years ago
  AND
    mag < 7.00 -- If apparent mag is greater than 7.00 star cannot be seen with naked eye

  ORDER BY dist_ly ASC;