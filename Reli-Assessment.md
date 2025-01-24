# Test Plan Development

## Points of Contacts
- Provide the contact information of all parties involved in this feature: Product Manager, Project Manager, Developers, QAs, Business team, Analytics, etc.

| Role       | Email             |
|------------|-------------------------|
| Role | Name (with a hyperlink to email): |
| Project Manager |  [Chris A](#) |
| Developers |  [Alex ](#) , [Sam](#) ,[Kathya ](#)|
| Analytics |  [Chris B](#) |
| QA |  [Chris C](#) |

## Allocation
**Bid optimization process**
- **Personel:** [Kathya ](#), [Alex ](#)
- **Role:** Subject matter experts for the original bid optimization process.
- **Responsibility:** Provide insights into existing workflows, logic validation, and expected outcomes.

**Performance Tables setup**
- **Personel:** [Sam](#)
- **Role:** Data pipeline expert for the new marketing stream hourly performance tables.
- **Responsibility:** Validate data accuracy and assist in resolving issues related to hourly performance metrics.

**QA Engineers**
- **Personel:** [Chris C](#)
- **Role:** Lead testing efforts, including test case design, execution, and reporting.

[Include all other invovled parties' responsibilities]

## Timeline

Keep track of all the changes in this Test Plan, including the status of the new feature development. This timeline table also provides if there's any blocker that interferes with the development progress

| Date       | Description             |
|------------|-------------------------|
| YYYY-MM-DD | Brief description here |
| YYYY-MM-DD | System was down, which introduced some blocker in testing the features. |
| YYYY-MM-DD | Update the Schedule table, deadline for UAT on Staging is extended for 1 week |

## Overview
| Date       | Status             |
|------------|-------------------------|
| YYYY-MM-DD | UAT completed on Staging | 

- Provide an overview of the feature, what to be implemented and its requirements. 
- Include any other links that related to this new features.
- **Scopes of Testings:**
  - Verify that keyword groups are accurately identified based on Short ID, Keyword Text, Match Type, and Campaign Type.
  - Ensure that bid optimizations are applied to groups only if there are at least 5 clicks.
  - Validate performance aggregation logic for all targets within a group.
  - Test scenarios with paused targets to confirm their inclusion in performance calculations.
  
## Schedule

- When the feature is addressed and discussed in the planning meeting
- The deadline when the feature is completed on the testing environments (integration, staging, etc.)
- The deadline when UAT is completed on the testing environments
- The deadline when the feature is pushed to Production.
- The deadline when UAT is completed on Production.
- The time period that the featured should be monitored and logged on Production to ensure no issues occurs.


  



