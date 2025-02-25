### User Guide

### User

#### Overview
---

A user that is not a technical lead of a project or a member of staff of MySCW has a restricted view of their compute and storage data consumption.

Upon successful login to MySCW, a user’s view will default to the homepage that will display the following four charts:

1. Efficiency per month.

<img src="img/efficiency-per-month-chart.png" alt="" height=400>

2. Number of jobs per month.

<img src="img/number-of-jobs-per-month-chart.png" alt="" height=400>

3. Rate of usage per month.

<img src="img/rate-of-usage-per-month-chart.png" alt="" height=400>

4. Cumulative total usage per month.

<img src="img/cumulative-total-usage-per-month-chart.png" alt="" height=400>

**Note:** All of the above charts will default to display the user’s usage over the last twelve months. 


#### Filter Chart Data
---

By default, the charts will display the cumulative totals of a user's usage for the projects in which a user has an approved project membership. A user can filter the results on a per-project basis by selecting the ‘Project Filter' dropdown option and selecting a project.

<img src="img/data-analytics-project-dropdown-filter.png" alt="" height=400>


### Technical Lead

#### Overview
---

In addition to the default users view as described in the ‘User' section above, a technical lead of a project will have the option to view the compute and storage consumption for their projects.

Upon successful login to MySCW, a technical lead will have an additional link in the left sidebar menu named ‘Data Analytics’.

<img src="img/data-analytics-link.png" alt="" height=350>

By default, the link will direct the user to the data analytics page of their most recently created project on MySCW.

<img src="img/data-analytics-link-with-project.png" alt="" height=300>


#### Filter Projects
---

Technical leads that are linked to multiple SCW projects can switch between projects by selecting the ‘Project Filter' dropdown option.

<img src="img/data-analytics-project-filter.png" alt="" height=200>

### Project Notifications

#### Overview
---
When a technical lead or member of staff views the data analytics for a given project, several background checks are performed. Should the project meet any of the criteria listed below, a notification is displayed on all the data analytics pages.

1. Check the home storage allocation usage is > 75%.
2. Check the scratch storage allocation usage is > 75%.
3. Check the allocated core hours usage is > 75%.

**Note:** Code for the checks above can be found within the `IndexView` of `stats/views.py`.

#### Example
---

<img src="img/data-analytics-project-notifications.png" alt="">

### Project Overview Data

<img src="img/data-analytics-overview-map.png" alt="">

<table>
    <thead>
        <tr>
            <th><strong>ID</strong></th>
            <th><strong>Title</strong></th>
            <th><strong>Description</strong></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>Principle Investigator</td>
            <td>Project’s PI name and institution.</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Technical Lead</td>
            <td>Project’s Technical Lead's name.</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Start date</td>
            <td>Project’s start date.</td>
        </tr>
        <tr>
            <td>4</td>
            <td>End date</td>
            <td>Project’s end date.</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Institution</td>
            <td>Project’s Technical Lead’s institution.</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Efficiency</td>
            <td>Project’s overall efficiency.</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Home storage allocation</td>
            <td>Project’s home storage allocation - N/A if empty.</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Scratch storage allocation</td>
            <td>Project’s scratch storage allocation - N/A if empty.</td>
        </tr>
        <tr>
            <td>9</td>
            <td>Total allocated core hours</td>
            <td>Project’s total allocated core hours.</td>
        </tr>
        <tr>
            <td>10</td>
            <td>Total number of core hours</td>
            <td>Project’s total number of elapsed core hours consumed over all time.</td>
        </tr>
        <tr>
            <td>11</td>
            <td>Total number of CPU hours</td>
            <td>Project’s total number of CPU hours consumed over all time.</td>
        </tr>
        <tr>
            <td>12</td>
            <td>Total number of Slurm jobs</td>
            <td>Project’s total number of jobs run through Slurm over all time.</td>
        </tr>
        <tr>
            <td>13</td>
            <td>Principal Investigator’s Projects chart</td>
            <td>Displays the number of active, dormant, inactive and retired projects for the project’s PI.</td>
        </tr>
        <tr>
            <td>14</td>
            <td>Users status chart</td>
            <td>Displays the number of active, dormant and inactive users for the project.</td>
        </tr>
    </tbody>
</table>

### Project Compute Data

<img src="img/data-analytics-compute-map.png" alt="">

<table>
    <thead>
        <tr>
            <th><strong>ID</strong></th>
            <th><strong>Title</strong></th>
            <th><strong>Description</strong></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>Start date</td>
            <td>Start date of the compute consumption query.</td>
        </tr>
        <tr>
            <td>2</td>
            <td>End date</td>
            <td>End date of the compute consumption query.</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Core Partitions data in date range</td>
            <td>CPU Time, Wait Time, Wall Time and Efficiency of the project on the <strong>core partitions</strong> within the query’s start and end date.</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Core Partitions data to present</td>
            <td>CPU Time, Wait Time, Wall Time and Efficiency of the project on the <strong>core partitions</strong> from the project start date to the present date.</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Researcher Funded Partitions data in date range</td>
            <td>CPU Time, Wait Time, Wall Time and Efficiency of the project on the <strong>researcher funded partitions</strong> within the query’s start and end date.</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Researcher Funded Partitions data to present</td>
            <td>CPU Time, Wait Time, Wall Time and Efficiency of the project on the <strong>researcher funded partitions</strong> from the project start date to present date.</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Core Partitions + Researcher Funded Partitions data in date range</td>
            <td>CPU Time, Wait Time, Wall Time and Efficiency of the project on the <strong>core partitions and researcher funded partitions</strong> within the query’s start and end date.</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Core Partitions + Researcher Funded Partitions data to present</td>
            <td>CPU Time, Wait Time, Wall Time and Efficiency of the project on the <strong>core partitions and researcher funded partitions</strong> from the project start date to present date.</td>
        </tr>
        <tr>
            <td>9</td>
            <td>Total Charge</td>
            <td>Set to N/A.</td>
        </tr>
    </tbody>
</table>

### Project Compute Charts

<img src="img/data-analytics-techlead-charts-1.png" alt="">

<img src="img/data-analytics-techlead-charts-2.png" alt="">

<table>
    <thead>
        <tr>
            <th><strong>ID</strong></th>
            <th><strong>Title</strong></th>
            <th><strong>Description</strong></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>Rate of usage per month</td>
            <td>Displays the CPU Time, Wait Time and Wall Time per month within the query’s start and end date.</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Cumulative total usage per month</td>
            <td>Displays the cumulative CPU Time, Wait Time and Wall Time per month within the query’s start and end date.</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Top 10 users usage</td>
            <td>Displays the top 10 users of the project by Wall Time within the query’s start and end date.</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Usage by partition</td>
            <td>Displays the usage of partitions within the query’s start and end date.</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Efficiency per month</td>
            <td>Displays the efficiency per month within the query’s start and end date.<br /><br />
                The table below the chart shows the average efficiency per month within the query’s start and end date as well
                as the project’s start date to the present date.</td>
        </tr>
        <tr>
            <td>6</td>
            <td>Number of jobs per month</td>
            <td>Displays the number of jobs per month within the query's start and end date.<br /><br />
                The table below the chart shows the total number of jobs within the query’s start and end date as well as
                the project’s start date to the present date.</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Per-Job average stats per month</td>
            <td>Displays the Per-Job average CPU Time, Wait Time and Wall Time per month within the query’s start and end date.<br /><br />
                The table below the chart shows the Per-Job average CPU Time, Wait Time
                and Wall Time per month within the query’s start and end date as well as the project’s start date to the present date.</td>
        </tr>
        <tr>
            <td>8</td>
            <td>Core count and node utilisation per month</td>
            <td>Displays the core count and node utilisation per month within the query’s start and end date.<br /><br />
                The table below the chart shows the number of cores and average number of cores per job
                per month within the query’s start and end date as well as the project’s start date to the present date.<br /><br />
                <strong>Note</strong>: Array jobs in the Compute Daily table display as using a
                single core with multiple jobs.</td>
        </tr>
    </tbody>
</table>

**Note**: The start and end date will default to the last twelve months if not defined by the user.

#### Filter Projects
---

Technical leads can filter the compute data analytics by partitions by selecting the ‘Partitions Filter' dropdown option.

<img src="img/data-analytics-partition-filter.png" alt="" height=350>

### Project Storage Data

<img src="img/data-analytics-storage-map.png" alt="">

<table>
    <thead>
        <tr>
            <th><strong>ID</strong></th>
            <th><strong>Title</strong></th>
            <th><strong>Description</strong></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>Start date</td>
            <td>Start date of the storage consumption query.</td>
        </tr>
        <tr>
            <td>2</td>
            <td>End date</td>
            <td>End date of the storage consumption query.</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Average disk space usage per week</td>
            <td>Average disk space usage per week for home and scratch within the query’s start and end date.</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Average file count per week</td>
            <td>Average file count per week for home and scratch within the query’s start and end date.</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Disk space per month chart</td>
            <td>Disk space usage per month for home and scratch within the query’s start and end date.</td>
        </tr>
        <tr>
            <td>6</td>
            <td>File count per month chart</td>
            <td>File count per month for home and scratch within the query’s start and end date.</td>
        </tr>
    </tbody>
</table>

**Note**: The start and end date will default to the last twelve months if not defined by the user.

### Staff

#### Overview
---

In addition to the default users view as described in the ‘User’ section above, a member of staff will have the option to view the compute and storage consumption of any project on MySCW.

Upon successful login to MySCW, a member of staff will have an additional link in the left sidebar menu named ‘Data Analytics’.

<img src="img/data-analytics-link.png" alt="" height=350>

By default, this link will direct the member of staff to a project search form. 

<img src="img/project-search-form.png" alt="">

The member of staff can then look up a project using an SCW, HPCW or ARCCA code. The returned data analytics view will be the same as described in the 'Technical User' section above.


### Data Export

#### Charts
---

All charts listed within these documents support multiple export formats. A list of supported formats is available by clicking the menu option found at the top right of a selected chart.

<img src="img/data-analytics-export-formats.png" alt="" height=350>

#### Project Summary
---

Technical leads and members of staff can generate and download a summary of the overview, compute and storage tabs found within the data analytics page for a project. The 'Export to PDF' button is located to the top left of the project title.

<img src="img/data-analytics-export-to-pdf.png" alt="">

