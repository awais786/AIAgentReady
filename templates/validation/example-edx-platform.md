# Worked Example — edx-platform Instantiation

The first instantiation of [questions.md](questions.md), used by the Phase 1 pilot
(`phase-1-edx-pilot`). Expected-answer notes are for the scorer, per
[rubric.md](rubric.md); they were drafted from prior knowledge of the repo and MUST be
verified against the pilot checkout (task: pilot review) before the "after" run is scored.

## Location

1. **Where is course enrollment implemented?**
   *Expect:* `CourseEnrollment` model (`common/djangoapps/student/models/course_enrollment.py`), especially `CourseEnrollment.enroll()`.
   *Source:* core learner flow; constant support topic.

2. **Where would a change to course-access rules (what lets a learner view courseware) need to be made?**
   *Expect:* `has_access` in `lms/djangoapps/courseware/access.py` (+ access response classes nearby).
   *Source:* recurring source of confusion in access-control bug reports.

3. **Which tests cover the grades app, and how do I run just those?**
   *Expect:* `lms/djangoapps/grades/tests/`, run via `pytest lms/djangoapps/grades`.
   *Source:* grading regressions are high-severity; contributors need this on day one.

4. **Where is the `FEATURES` settings dict defined, and where is one of its flags consumed?**
   *Expect:* defined in `lms/envs/common.py` (and `cms/envs/common.py` for Studio), consumed via `settings.FEATURES[...]` at call sites; newer toggles use `edx-toggles` waffle classes.
   *Source:* first thing an operator touches when configuring an instance.

## Behavior

5. **How does learner enrollment work end to end, from the enroll action to the learner being enrolled?**
   *Expect:* enrollment view/API → `CourseEnrollment.enroll()` → mode/state checks → enrollment signal(s) firing downstream (e.g. email, analytics).
   *Source:* the design doc's canonical example flow.

6. **What happens when a learner submits an answer to a problem?**
   *Expect:* XBlock handler request → capa problem grading → learner state saved (`StudentModule`) → score-changed signal → asynchronous grade recalculation (grades app / celery).
   *Source:* spans three subsystems; classic new-contributor stumbling block.

7. **How do the LMS and Studio (CMS) share course content?**
   *Expect:* both read the modulestore (`xmodule/modulestore`, split-Mongo draft/published branches); Studio authors drafts, publishing makes content visible to LMS.
   *Source:* the central architectural fact of the platform.

## Rationale

8. **Why does the CCX app (`lms/djangoapps/ccx`) exist?**
   *Expect:* Custom Courses for edX — lets an instructor run a scheduled, gated subset of an existing course for their own cohort without duplicating content; supported by citation to docs/PRs.
   *Source:* module whose name explains nothing; pure tribal knowledge.

9. **Why are grades stored in persistent tables and recalculated asynchronously instead of computed on request?**
   *Expect:* on-the-fly grading did not scale for large courses; persistent grades (`PersistentCourseGrade` et al.) traded freshness for performance; supported by citation.
   *Source:* surprising-pattern question; the naïve approach looks simpler and was in fact abandoned.

10. **What is risky to change in the modulestore, and why?**
    *Expect:* draft/published branch semantics, structure documents/versioning, anything consumed by both LMS and Studio; past breakage and broad blast radius; supported by citation or documented incident.
    *Source:* the platform's highest-coupling area.

## Distribution check

4 location / 3 behavior / 3 rationale — matches the template. Fixed before the pilot's
"before" run; do not edit afterwards.
