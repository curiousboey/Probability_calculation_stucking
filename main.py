import numpy as np
import matplotlib.pyplot as plt

steps =[]
x_points = []
num_of_box = 10000
iteration_per_box = 10

for l in range(num_of_box):
    avg_steps = []
    x_points.append(l+1)

    for l1 in range(iteration_per_box):
        length_of_cube = l + 1
        start = [0, 0]
        div_len = length_of_cube / 2

        random_walk = ([-1, 0], [0, 1], [1, 0], [-1, -1])
        points = []
        points.append(start)

        while random_walk != []:
            random_walk = ([-1, 0], [0, 1], [1, 0], [0, -1])
            r = random_walk[int(np.random.randint(0, 4, 1))]
            new_point = [a + b for a, b in zip(points[len(points) - 1], r)]  # element wise additions
            j = 0
            for i in range(len(points)):
                if (points[i] != new_point and abs(new_point[0]) < div_len and abs(new_point[1]) < div_len):
                    j += 1
                else:
                    pass

            if (len(points) == j and abs(new_point[0]) < div_len and abs(new_point[1]) < div_len):
                points.append(new_point)
            else:
                random_walk = list(random_walk)
                random_walk.remove(r)
                random_walk = tuple(random_walk)
                r = random_walk[int(np.random.randint(0, 3, 1))]
                new_point = [a + b for a, b in zip(points[len(points) - 1], r)]  # element wise additions
                j = 0
                for i in range(len(points)):
                    if (points[i] != new_point and abs(new_point[0]) < div_len and abs(new_point[1]) < div_len):
                        j += 1
                    else:
                        pass
                if (len(points) == j and abs(new_point[0]) < div_len and abs(new_point[1]) < div_len):
                    points.append(new_point)
                else:
                    random_walk = list(random_walk)
                    random_walk.remove(r)
                    random_walk = tuple(random_walk)
                    r = random_walk[int(np.random.randint(0, 2, 1))]
                    new_point = [a + b for a, b in zip(points[len(points) - 1], r)]  # element wise additions
                    j = 0
                    for i in range(len(points)):
                        if (points[i] != new_point and abs(new_point[0]) < div_len and abs(new_point[1]) < div_len):
                            j += 1
                        else:
                            pass
                    if (len(points) == j and abs(new_point[0]) < div_len and abs(new_point[1]) < div_len):
                        points.append(new_point)
                    else:
                        random_walk = list(random_walk)
                        random_walk.remove(r)
                        random_walk = tuple(random_walk)
                        r = random_walk[int(np.random.randint(0, 1, 1))]
                        new_point = [a + b for a, b in zip(points[len(points) - 1], r)]  # element wise additions
                        j = 0
                        for i in range(len(points)):
                            if (points[i] != new_point and abs(new_point[0]) < div_len and abs(new_point[1]) < div_len):
                                j += 1
                            else:
                                pass
                        if (len(points) == j and abs(new_point[0]) < div_len and abs(new_point[1]) < div_len):
                            points.append(new_point)
                        else:
                            random_walk = []
        avg_steps.append(len(points)-1)

    steps.append(sum(avg_steps)/iteration_per_box)
    print('Total steps for length',length_of_cube,"are= ", steps[l], "steps")

plt.plot(x_points, steps,color='red', linestyle='solid', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=2)
plt.grid()






