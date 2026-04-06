
#function to calculate the mean of the ratings
def median_caculation(rating_datas):
  rating_data.sort() #sort the list of rates
  count = len(rating_data)

#finding the median
if count % 2 == 1:
  return rating_data[count // 2] #odd number of datas
else:
  middle1 = rating_data[(count // 2) - 1]
  middle2 = rating_data[count // 2]
  return (middle1 + middle2) / 2 #even number of datas
