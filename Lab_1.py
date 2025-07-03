import numpy as np

# Create the 4x4 student_scores array (Math, Science, English, History)
student_scores = np.array([
    [85, 78, 92, 70],
    [76, 88, 90, 65],
    [90, 72, 85, 80],
    [70, 95, 88, 75]
])

# Calculate the average score for each subject (column-wise)
subject_averages = np.mean(student_scores, axis=0)

# List of subject names
subject_names = ['Math', 'Science', 'English', 'History']

# Find the subject with the highest average score
highest_avg_index = np.argmax(subject_averages)

# Print results
print("Average scores for each subject (Math, Science, English, History):")
print(subject_averages)
print("Subject with the highest average score:", subject_names[highest_avg_index])
