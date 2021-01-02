from typing import List
def calculate_waiting_times(duration_times: List[int]) -> List[int]:
    waiting_times = [0] * len(duration_times)
    for i in range(1, len(duration_times)):
        waiting_times[i] = duration_times[i - 1] + waiting_times[i - 1]
    return waiting_times

def calculate_turnaround_times(
    duration_times: List[int], waiting_times: List[int]
) -> List[int]:
        return [
        duration_time + waiting_times[i]
        for i, duration_time in enumerate(duration_times)
    ]


def calculate_average_turnaround_time(turnaround_times: List[int]) -> float:
    return sum(turnaround_times) / len(turnaround_times)


def calculate_average_waiting_time(waiting_times: List[int]) -> float:
    return sum(waiting_times) / len(waiting_times)


if __name__ == "__main__":
    # process id's
    processes = [1, 2, 3]

    # ensure that we actually have processes
    if len(processes) == 0:
        print("Zero amount of processes")
        exit()

    # duration time of all processes
    duration_times = [19, 8, 9]

    # ensure we can match each id to a duration time
    if len(duration_times) != len(processes):
        print("Unable to match all id's with their duration time")
        exit()

    # get the waiting times and the turnaround times
    waiting_times = calculate_waiting_times(duration_times)
    turnaround_times = calculate_turnaround_times(duration_times, waiting_times)

    # get the average times
    average_waiting_time = calculate_average_waiting_time(waiting_times)
    average_turnaround_time = calculate_average_turnaround_time(turnaround_times)

    # print all the results
    print("Process ID\tDuration Time\tWaiting Time\tTurnaround Time")
    for i, process in enumerate(processes):
        print(
            f"{process}\t\t{duration_times[i]}\t\t{waiting_times[i]}\t\t{turnaround_times[i]}"
        )
    print(f"Average waiting time = {average_waiting_time}")
    print(f"Average turn around time = {average_turnaround_time}")
