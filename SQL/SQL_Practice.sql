--1.	Combine Two Tables
--(1)	ʹ��OUTER JOIN����ֻ������û��ַ�����
SELECT Person.FirstName, Person.LastName, Address.City, Address.State FROM Person
LEFT JOIN Address ON Person.PersonID = Address.PersonID

--2.	Second Highest Salary
--(1)	ʹ��SELECTǶ�ף�����û�еڶ��ߵĹ��ʣ����NULL
--(2)	ʹ��DISTICNT������ֻ���������й��ʣ����ʻ���ͬ��Ҳû�еڶ��ߵĹ���
--(3)	ʹ��OFFSET���ӵڶ�λ��ʼ��LIMIT
SELECT(
    SELECT DISTINCT Salary FROM Employee
    ORDER BY Salary DESC
    LIMIT 1 OFFSET 1
) AS SecondHighestSalary
