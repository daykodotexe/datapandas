import json

STATUS_ORDER = {"PASS": 0, "WARN": 1, "FAIL": 2}


class Report:
    def __init__(self, checks):
        self.checks = checks
        self.status = self._compute_status()

        failed = []
        for name, c in checks.items():
            if c["status"] == "FAIL":
                failed.append(name)

        self.failed_checks = failed

    def _compute_status(self):
        worst = "PASS"
        for c in self.checks.values():
            if STATUS_ORDER[c["status"]] > STATUS_ORDER[worst]:
                worst = c["status"]
        return worst

    def summary(self):
        print(f"Overall Status: {self.status}")
        for name, c in self.checks.items():
            print(f"- {name}: {c['status']} ({c['message']})")

    def to_json(self, path):
        with open(path, "w") as f:
            json.dump(
                {
                    "status": self.status,
                    "checks": self.checks
                },
                f,
                indent=2
            )