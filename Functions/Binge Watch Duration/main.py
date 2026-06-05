def calculate_duration(number_of_episodes, average_episode_length_minutes):
    total_length = number_of_episodes * average_episode_length_minutes
    return total_length

def main():
    number_of_episodes = int(input("Amount of episodes: "))
    average_episode_length = int(input("average episode length in minutes: "))
    print(f"Total length of binge watch: {calculate_duration(number_of_episodes, average_episode_length)} minutes.")

main()
