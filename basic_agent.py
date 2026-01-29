from spade.agent import Agent
from spade.behaviour import OneShotBehaviour
import asyncio

class SensorAgent(Agent):
    class HelloBehaviour(OneShotBehaviour):
        async def run(self):
            print(f"Hello! I am {self.agent.name}")

    async def setup(self):
        print(f"{self.name} starting...")
        self.add_behaviour(self.HelloBehaviour())

async def main():
    # Replace these with your XMPP credentials
    agent_jid = "sensoragent2005@xmpp.jp"
    agent_password = "Ilovechrist123"

    sensor_agent = SensorAgent(agent_jid, agent_password)
    await sensor_agent.start(auto_register=True)  
    print("Agent started!")

    try:
        while sensor_agent.is_alive():
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        print("Stopping agent...")
    await sensor_agent.stop()

if __name__ == "__main__":
    asyncio.run(main())



