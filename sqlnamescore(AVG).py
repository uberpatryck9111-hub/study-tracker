SELECT students.name, ROUND(AVG(scores.score), 2) AS average
FROM students
JOIN scores ON students.id = scores.student_id
GROUP BY students.name
ORDER BY average DESC;