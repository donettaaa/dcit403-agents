# LAB 2: SensorAgent with perception
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
import asyncio
import datetime
import random

# Simulated environment
environment = {
    "flood_level": 0,
    "fire_level": 0,
    "earthquake_level": 0
}

# Function to generate a random disaster
def generate_disaster_event():
    event_type = random.choice(["flood", "fire", "earthquake"])
    severity = random.randint(1, 5)
    environment[f"{event_type}_level"] = severity
    return event_type, severity

# SensorAgent class
class SensorAgent(Agent):
    class SenseEnvironmentBehaviour(CyclicBehaviour):
        async def run(self):
            event, severity = generate_disaster_event()
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_message = f"[{timestamp}] Detected {event} with severity {severity}"
            print(log_message)
            
            # Save to event log file
            with open("event_log.txt", "a") as f:
                f.write(log_message + "\n")
            
            await asyncio.sleep(5)

    async def setup(self):
        print(f"{self.name} starting...")
        self.add_behaviour(self.SenseEnvironmentBehaviour())

# Run the agent
async def main():
    agent_jid = "sensoragent2005@xmpp.jp"   
    agent_password = "Ilovechrist123"      

    sensor_agent = SensorAgent(agent_jid, agent_password)
    await sensor_agent.start(auto_register=True)
    print("SensorAgent started!")

    try:
        while sensor_agent.is_alive():
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        print("Stopping agent...")
    await sensor_agent.stop()

if __name__ == "__main__":
    asyncio.run(main())


