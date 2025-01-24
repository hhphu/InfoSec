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

| Date       | Status             |
|------------|-------------------------|
| YYYY-MM-DD | When the feature is addressed and discussed in the planning meetings | 
| YYYY-MM-DD | The deadline when the feature is completed on the testing environments (integration, staging, etc.) | 
| YYYY-MM-DD | The deadline when UAT is completed on the testing environments| 
| YYYY-MM-DD | The deadline when the feature is pushed to Production. | 
| YYYY-MM-DD | The deadline when UAT is completed on Production.| 
| YYYY-MM-DD | The time period that the featured should be monitored and logged on Production to ensure no issues occurs. | 


## Risk Factors
### 1. Inaccurate or incomplete data in the hourly performance tables or the keyword_multivers database could result in incorrect bid optimizations. This includes:
- Missing or inconsistent performance metrics for specific time windows.
- Errors in aggregating performance data at the group level (Short ID, Keyword Text, Match Type, Campaign Type).
- Misaligned paused targets, leading to invalid or outdated bid updates.
  
**Impact**
- Incorrect bid optimizations could lead to overspending or missed opportunities in advertising campaigns.
- Performance metrics used for decision-making may be unreliable, potentially affecting future strategies.
  
**Mitigations**
- Implement automated data validation scripts to check for missing or anomalous data in hourly performance tables and group aggregations.
- Establish alerts in monitoring tools to flag abnormal data patterns.
- Conduct end-to-end data validation tests as part of the QA process, ensuring that inputs, processing, and outputs align with expectations.
- Include edge case testing for scenarios such as missing time windows or paused targets.
- Set up CI/CD pipelines to reduce testing effort
  
### 2. Underperformance under hig load
During peak hours, the feature may not perform very well due to its inability to handl high load. There maybe delays/failures to calculate bids update sufficiently during high traffic hours

**Impact**
- The overall ad performance can be affected due to the delays in calculate bids
- Slower system response times can implact downstream process and user experience
- This can cause potential downtime/crashes on the server sides.
- This also leads to potential loss in revenue and opportunities to faciliates sales.
  
**Mitigation**
- Conduct performance and stress tests using tools like Apache JMeter or Locust to simulate high traffic scenarios and identify bottlenecks.
- Ensure the infrastructure is scalable by leveraging cloud-based solutions or distributed systems to handle increasing loads effectively.
- Optimize database queries, adding indexes to improve query performance for large datasets.
- Cache frequently accessed data, especially for group-level performance metrics and hourly aggregations.
- Set up real-time monitoring for system performance, with alerts for slow query times, memory usage, and processing delays.

### 3. Outliers within groups can skew effective bid calculations, leading to suboptimal optimizations. Specifically:
- Aggregating performance metrics across targets with significantly different behaviors may distort bid adjustments.
- Paused targets with outdated or irrelevant data may inadvertently influence group-level decisions.
  
**Impact**
- This may result in  financial losses due to either overbidding or underbidding.
- Mismanagement of paused targets may lead to incorrect bid updates being applied, causing further inefficiencies.

**Mitigation**
- Implement logic to exclude outliers and appropriately weight data from paused targets based on recency and relevance.
- Define clear thresholds for identifying and handling outliers 
- Regularly review and update rules as business needs evolve.
- Develop test cases that specifically target scenarios involving extreme outliers, paused targets, and groups with varying bid behaviors.
- Validate effective bid calculations using multiple methods (e.g., average bid, most common bid) to ensure robustness.

## Methodologies
### Functional Testing
- Validate the correctness of bid optimization logic, including group-based optimizations, effective bid calculations, and time-based bidding strategies.

### Regression Testing
- Ensure that updates to the bid optimization framework do not negatively impact existing features or workflows.

### Performance Testing
- Measure system behavior under high data loads and ensure timely processing of bid adjustments, especially during peak traffic periods.

### Integration Testing
- Verify seamless integration between the bid optimization framework and new hourly performance tables, as well as the keyword_multivers database.

### Database Testing
- Validate accurate data retrieval, updates, and consistency in performance metrics and bid updates.

### Exploratory Testing
- Identify edge cases and unforeseen issues by exploring the system without predefined test scripts.

### User Acceptance Testing (UAT)
- To confirm that the new functionality meets business needs and expectations, involving Alex, Kathya, and Sam as reviewers.



