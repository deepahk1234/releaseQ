import json

# Based on the images I can see, I'll extract the data structure and metrics
dashboard_data = {
    "performance_metrics": {
        "application_performance": {
            "response_time": {"current": 245, "target": 300, "unit": "ms", "status": "pass"},
            "throughput": {"current": 1200, "target": 1000, "unit": "req/s", "status": "pass"},
            "error_rate": {"current": 0.02, "target": 0.1, "unit": "%", "status": "pass"},
            "memory_usage": {"current": 78, "target": 80, "unit": "%", "status": "pass"}
        }
    },
    "technical_debt": {
        "breakdown": {
            "high_priority": {"value": 2.1, "unit": "hours"},
            "medium_priority": {"value": 4.2, "unit": "hours"},
            "low_priority": {"value": 6.8, "unit": "hours"},
            "total_debt": {"value": 13.1, "unit": "hours"}
        },
        "hotspots": [
            {"name": "Authentication Module", "type": "Refactoring needed", "effort": 2.5},
            {"name": "Data Processing", "type": "Performance optimization", "effort": 1.8},
            {"name": "API Gateway", "type": "Code duplication", "effort": 1.2}
        ]
    },
    "code_quality": {
        "trends": {
            "v2.6": 80,
            "v2.5": 75,
            "v2.4": 72,
            "v2.3": 68,
            "v2.2": 65,
            "v2.1": 58
        },
        "improvement": 22,
        "cognitive_complexity": {"current": 1204, "previous": 1189, "change": 15}
    },
    "security_compliance": {
        "standards": {
            "owasp_top10": "Compliant",
            "cwe_top25": "Addressed", 
            "nist_guidelines": "Following",
            "soc2": {"status": "In progress", "completion": 85}
        },
        "dependency_security": {
            "total_dependencies": 142,
            "up_to_date": 134,
            "up_to_date_percentage": 94,
            "minor_updates": 6,
            "major_updates": 2,
            "vulnerabilities": 0
        },
        "security_score": 98,
        "scan_results": {
            "snyk": {"status": "Pass", "critical": 0, "high": 0, "medium": 2, "low": 5},
            "sonarqube": {"status": "Pass", "critical": 0, "high": 1, "medium": 3, "low": 12},
            "owasp_dependency": {"status": "Review", "critical": 0, "high": 0, "medium": 1, "low": 8},
            "codeql": {"status": "Pass", "critical": 0, "high": 0, "medium": 0, "low": 4}
        },
        "vulnerability_summary": {
            "critical": 0,
            "high": 1,
            "medium": 6,
            "low": 29
        }
    },
    "testing_qa": {
        "test_coverage": {
            "unit_tests": 82,
            "integration": 74,
            "e2e_tests": 65,
            "api_tests": 91
        },
        "quality_gates": {
            "build": "Passing (All platforms)",
            "unit_tests": "1,247 tests passed",
            "code_coverage": "Above threshold (80%+)",
            "security_scan": "No critical issues",
            "performance": "1 regression identified",
            "dependencies": "Up to date"
        }
    },
    "sonarqube_metrics": {
        "bugs": {"current": 3, "previous": 7, "change": -4},
        "vulnerabilities": {"current": 1, "previous": 2, "change": -1},
        "code_smells": {"current": 47, "previous": 52, "change": -5},
        "duplicated_lines": {"current": 2.1, "previous": 2.8, "change": -0.7},
        "cognitive_complexity": {"current": 1204, "previous": 1189, "change": 15}
    },
    "audit_trail": {
        "recent_audits": [
            {"type": "Security Audit", "date": "2024-09-15", "status": "Passed"},
            {"type": "Code Review", "date": "2024-09-20", "status": "Approved"},
            {"type": "Penetration Test", "date": "2024-09-10", "status": "Minor findings"},
            {"type": "Compliance Check", "date": "2024-09-18", "status": "Compliant"}
        ],
        "action_items": [
            "Address medium priority security findings by 2024-10-01",
            "Increase E2E test coverage to 75% by 2024-10-15",
            "Complete SOC 2 compliance documentation",
            "Resolve performance regression in data processing"
        ]
    },
    "improvement_goals": {
        "code_coverage": {"current": 85, "target": 90, "owner": "QA Team", "due": "2024-10-30"},
        "security_score": {"current": 98, "target": 100, "owner": "Security Team", "due": "2024-10-15"},
        "technical_debt": {"current": "13.1h", "target": "<10h", "owner": "Dev Team", "due": "2024-11-15"},
        "performance": {"current": "Good", "target": "Excellent", "owner": "Platform Team", "due": "2024-10-30"}
    }
}

def generate_md_report(data):
    """Generates a Markdown report from the dashboard data."""
    report = "# Development Quality Dashboard Report\n\n"

    for section, values in data.items():
        report += f"## {section.replace('_', ' ').title()}\n\n"
        if isinstance(values, dict):
            for key, value in values.items():
                report += f"### {key.replace('_', ' ').title()}\n"
                if isinstance(value, dict):
                    for sub_key, sub_value in value.items():
                        report += f"- **{sub_key.replace('_', ' ').title()}:** {sub_value}\n"
                elif isinstance(value, list):
                    for item in value:
                        if isinstance(item, dict):
                            report += "- " + ", ".join([f"{k.replace('_', ' ').title()}: {v}" for k, v in item.items()]) + "\n"
                        else:
                            report += f"- {item}\n"
                else:
                    report += f"- {value}\n"
                report += "\n"
        report += "\n"

    return report

def generate_rst_report(data):
    """Generates a reStructuredText report from the dashboard data."""
    report = "================================\n"
    report += "Development Quality Dashboard Report\n"
    report += "================================\n\n"

    for section, values in data.items():
        report += f"{section.replace('_', ' ').title()}\n"
        report += "-" * len(section) + "\n\n"
        if isinstance(values, dict):
            for key, value in values.items():
                report += f"{key.replace('_', ' ').title()}\n"
                report += "~" * len(key) + "\n"
                if isinstance(value, dict):
                    for sub_key, sub_value in value.items():
                        report += f"- **{sub_key.replace('_', ' ').title()}:** {sub_value}\n"
                elif isinstance(value, list):
                    for item in value:
                        if isinstance(item, dict):
                            report += "- " + ", ".join([f"{k.replace('_', ' ').title()}: {v}" for k, v in item.items()]) + "\n"
                        else:
                            report += f"- {item}\n"
                else:
                    report += f"- {value}\n"
                report += "\n"
        report += "\n"

    return report

if __name__ == "__main__":
    # Generate Markdown report
    md_report = generate_md_report(dashboard_data)
    with open("report.md", "w") as f:
        f.write(md_report)

    # Generate reStructuredText report
    rst_report = generate_rst_report(dashboard_data)
    with open("docs/report.rst", "w") as f:
        f.write(rst_report)

    print("Dashboard data structure created successfully")
    print(f"Total sections: {len(dashboard_data)}")
    print("Successfully generated report.md and report.rst")