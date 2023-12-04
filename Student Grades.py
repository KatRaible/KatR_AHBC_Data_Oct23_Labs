import numpy as np
import scipy

grades = np.array([
    [11, 9, 16, 13.5],
    [12, 11, 8.5, 10],
    [11, 18, 11.5, 9],
    [7, 15.5, 11, 14],
    [9.5, 12, 10.5, 14],
    [15, 18.5, 7, 12],
    [18, 15.5, 11, 7.5]
])

mean_subjects = np.mean(grades, axis=0)
print("Mean for each subject:", mean_subjects)


median_math = np.median(grades[:, 0])
print("Median grade in Math:", median_math)


from scipy import stats
mode_history = stats.mode(grades[:, 3])

print("Mode for History:", mode_history.mode[0])


correlation_matrix = np.corrcoef(grades, rowvar=False)


strongest_correlation_indices = np.unravel_index(np.argmax(np.abs(correlation_matrix - np.eye(4))), correlation_matrix.shape)


subjects = ["Math", "Science", "Reading", "History"]
subject1, subject2 = subjects[strongest_correlation_indices[0]], subjects[strongest_correlation_indices[1]]
print(f"The two subjects with the strongest correlation are: {subject1} and {subject2}")

def desc_stats(data):
    mean = np.mean(data)
    median = np.median(data)
    mode = stats.mode(data)
    minimum = np.min(data)
    maximum = np.max(data)
    range_val = maximum - minimum
    variance = np.var(data)
    std_dev = np.std(data)
    
    print("mean:", mean)
    print("median:", median)
    print("mode:", mode.mode[0])
    print("minimum:", minimum)
    print("maximum:", maximum)
    print("range:", range_val)
    print("variance:", variance)
    print("standard deviation:", std_dev)


exam_scores = [24, 5, 15, 60, 54, 82, 99, 80, 70, 98, 93, 60, 33, 22, 65, 61, 51, 58, 83, 86, 42, 67, 60]


desc_stats(exam_scores)
