# select crosstab by column and convert to percentile per race
nocov_13 = coverage_by_race_13['no']
no_insured_13 = nocov_13/nocov_13.ix['coltotal', 'rowtotal']
white_no_insured_13 = no_insured_13[0]

nocov_13 = coverage_by_race_13['no']
black_insured_13 = nocov_13/nocov_13.ix['coltotal', 'rowtotal']
no_black_insured_13 = black_insured_13[1]

nocov_13 = coverage_by_race_13['no']
am_in_insured_13 = nocov_13/nocov_13.ix['coltotal', 'rowtotal']
no_am_in_insured_13 = am_in_insured_13[2]

nocov_13 = coverage_by_race_13['no']
alaska_insured_13 = nocov_13/nocov_13.ix['coltotal', 'rowtotal']
no_alaska_insured_13 = alaska_insured_13[3]

nocov_13 = coverage_by_race_13['no']
catch_all_insured_13 = nocov_13/nocov_13.ix['coltotal', 'rowtotal']
no_catch_all_insured_13 = catch_all_insured_13[4]

nocov_13 = coverage_by_race_13['no']
asian_insured_13 = nocov_13/nocov_13.ix['coltotal', 'rowtotal']
no_asian_insured_13 = asian_insured_13[5]

nocov_13 = coverage_by_race_13['no']
pac_isl_insured_13 = nocov_13/nocov_13.ix['coltotal', 'rowtotal']
no_pac_isl_insured_13 = pac_isl_insured_13[6]

nocov_13 = coverage_by_race_13['no']
other_insured_13 = nocov_13/nocov_13.ix['coltotal', 'rowtotal']
no_other_insured_13 = other_insured_13[7]

nocov_13 = coverage_by_race_13['no']
twoplus_insured_13 = nocov_13/nocov_13.ix['coltotal', 'rowtotal']
no_twoplus_insured_13 = twoplus_insured_13[8]
