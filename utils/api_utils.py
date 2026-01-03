class apiUtils:
    def select_policy_by_response(response):
        job = response.json()["job"]
        if (job == "Manager"):
            print("Policy: Business Class Allowed")

        elif (job == "Intern"):
            print("Policy: Economy Only")

        else:
            print(f"{job} found at response ")

        return job
