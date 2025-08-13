
# Data Quality Checklist for Ingestion

## Schema & Keys
- Primary keys unique: members.member_id, sessions.session_id, attendance.attendance_id, wellness_programs.program_id, program_enrollments.enrollment_id, engagement_events.event_id
- Foreign keys valid: attendance.member_id→members, attendance.session_id→sessions, program_enrollments.member_id→members, program_enrollments.program_id→wellness_programs, engagement_events.member_id→members

## Required Fields & Enums
- Required columns present & non-null
- Enums enforced:
  - members.status ∈ {active, paused, cancelled}
  - attendance.status ∈ {attended, no_show, cancelled}
  - program_enrollments.status ∈ {active, dropped, completed}
  - engagement_events.event_type ∈ {app_open, workout_logged, goal_completed, article_view}
  - channel ∈ {mobile_app, web, email, kiosk}

## Types & Timestamps
- ISO-8601 dates/times; start < end; join_date ≤ today
- Email format, phone E.164

## Duplicates/Outliers/Nulls
- No duplicate PKs; deduplicate exact rows
- Investigate extreme dwell times & event bursts
- Handle missing optional data appropriately

## Referential & Temporal Integrity
- Enrollment within program window
- Attendance within session window ±15m
- Engagement after join_date
