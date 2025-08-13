
# Data Dictionary – ThreeSixty (Analytics-Focused)
Describe each field and business meaning. Add ranges, enums, and examples.

## members
- member_id (PK) – integer, unique
- first_name, last_name – strings
- email – string (E.164 phone in `phone`)
- gender – {M, F, Other}
- birth_date – date
- join_date – date
- membership_plan – {Gold, Silver, Basic, ...}
- status – {active, paused, cancelled}

## sessions
- session_id (PK) – integer
- session_name – string
- session_type – {class, PT, open_gym, ...}
- coach_id – FK → coaches.coach_id
- location – string
- start_datetime, end_datetime – timestamp
- capacity – integer >= 0

## attendance
- attendance_id (PK) – integer
- member_id – FK → members
- session_id – FK → sessions
- checkin_time, checkout_time – timestamp
- status – {attended, no_show, cancelled}
- source – {kiosk, mobile, staff}

## subscriptions
- subscription_id (PK), member_id FK, plan, start_date, end_date, status

## coaches
- coach_id (PK), name, specialty, rating (0–5), availability

## feedback
- feedback_id (PK), member_id FK, text, rating (1–5), created_at

## queries
- query_id (PK), member_id FK, text, created_at, intent (if labeled)

## wellness_programs / program_enrollments / engagement_events
- See ERD for fields and relations.
