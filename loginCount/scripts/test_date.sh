# Get the current date in YYYY-MM-DD format
current_date=$(date +%Y-%m-%d)

# Extract the day and month from the date
day=$(date -d "$current_date" +%d)
month=$(date -d "$current_date" +%m)

# Check if the day is between 1 and 7
# Remove leading 0 (ex. 09 -> 9)
day=${day#0}
if [[ $day -ge 1 && $day -le 7 ]]; then
  # Calculate the new month (subtract 1, wrap around to 12 if necessary)
  new_month=$((month - 1))
  if [[ $new_month -eq 0 ]]; then
    new_month=12
  fi
  day="0$day"
  # Create the new date with the adjusted month
  new_date=$(date -d "$year-$new_month-01" +%Y-%m-%d)
  echo $new_date
  start=$(new_date +\%Y)-$(new_date +\%m)-$(new_date --date "-8 days" +\%d)
else
  day="0$day"
  start=$(date +\%Y)-$(date +\%m)-$(date --date "-8 days" +\%d)
fi

echo $start


