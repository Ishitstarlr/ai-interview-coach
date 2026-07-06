class JDMatcher:

    def match(self, resume_data, jd_data):

        resume_skills = set(resume_data["skills"])

        jd_skills = set(jd_data["skills"])

        matched = resume_skills & jd_skills

        missing = jd_skills - resume_skills

        score = 0

        if len(jd_skills) > 0:
            score = round(len(matched) / len(jd_skills) * 100, 2)

        return {

            "match_score": score,

            "matched_skills": sorted(matched),

            "missing_skills": sorted(missing)

        }