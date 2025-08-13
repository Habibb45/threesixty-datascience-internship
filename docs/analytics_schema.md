
# Analytics Star Schema (Reporting Layer)

## Dimensions
- dim_member(member_id, gender, birth_date, age_bucket, join_date, membership_plan, status)
- dim_time(date_key, date, week, month, quarter, year, dow, is_weekend)
- dim_session(session_id, session_name, session_type, coach_name, location, capacity)
- dim_program(program_id, program_name, category, start_date, end_date)
- dim_channel(channel_key, channel_name)

## Facts
- fact_attendance(date_key, member_id, session_id; attended_flag, no_show_flag, dwell_minutes, checkin_minute_of_day)
- fact_engagement(date_key, member_id, channel_key; app_opens, workouts_logged, goals_completed, articles_viewed, total_events)
- fact_program_participation(date_key, member_id, program_id; enrollments, active_days, drops, completions)

## Core Metrics
- DAU/WAU/MAU, App opens per MAU, workouts per active member
- Attendance rate, No-show rate, Avg dwell, Coach utilization
- Program enrollment/completion/drop rates, retention
