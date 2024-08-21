Postmortem: Service Outage on August 10, 2024
Issue Summary:

Duration: August 10, 2024, 14:30 - 16:45 UTC
Impact: The API service handling user authentication was down. Users experienced authentication failures, resulting in login issues. Approximately 60% of our users were affected during this period.
Root Cause: A memory leak in the authentication service due to an unhandled edge case in the session management code.
Timeline:

14:30 UTC: Issue detected by monitoring alert indicating high latency and increased error rates in the authentication service.
14:35 UTC: The on-call engineer reviewed the alert and confirmed authentication failures. A customer complaint was also received through support channels.
14:40 UTC: Initial investigation revealed high memory usage in the authentication service. Assumption was made that this might be a result of increased traffic or a misconfiguration.
14:50 UTC: Investigated load balancer logs and found no anomalies. Suspected a potential DDoS attack and began checking firewall settings.
15:10 UTC: Escalated to the infrastructure team for further analysis. They confirmed that the load was within expected limits and there was no evidence of an attack.
15:30 UTC: Noticed that the authentication service had a high memory footprint. The application team was brought in to investigate the code.
15:45 UTC: Identified a memory leak in the session management code where session objects were not being garbage collected properly.
16:00 UTC: Applied a temporary fix by restarting the authentication service to clear the memory.
16:15 UTC: Implemented a permanent code fix by updating the session management code to ensure proper garbage collection.
16:45 UTC: Authentication service was fully operational again. Monitoring showed normal error rates and latency.
Root Cause and Resolution:

Root Cause: The issue was caused by a memory leak in the authentication service. Specifically, an edge case in the session management logic led to session objects not being released, which caused the service to exhaust available memory.

Resolution:

The temporary resolution involved restarting the authentication service to clear the accumulated memory.
For the permanent fix, the session management code was revised to ensure proper handling and release of session objects. Additional tests were conducted to verify that the issue was resolved and that similar edge cases were handled.
Corrective and Preventative Measures:

Improvements:

Code Review: Implement more rigorous code review practices, especially for critical components like session manage![image](https://github.com/user-attachments/assets/80801cc9-4b2b-40c5-b5f7-aa7d80523c3d)
ment.
Automated Testing: Enhance automated tests to cover edge cases and stress-test memory management.
Monitoring: Improve memory usage monitoring with real-time alerts for abnormal memory growth patterns.
Tasks:

Patch Code: Update session management code to fix memory leak issue (Assigned to Dev Team, Due: August 12, 2024).
Enhance Tests: Add unit tests and integration tests to cover edge cases in session management (Assigned to QA Team, Due: August 15, 2024).
Update Monitoring: Configure additional monitoring for memory usage and set up alerts for memory anomalies (Assigned to DevOps Team, Due: August 17, 2024).
This postmortem outlines the incident's key details, root causes, and corrective measures taken to prevent future occurrences.
