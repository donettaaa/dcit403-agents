from spade.agent import Agent
from spade.behaviour import FSMBehaviour, State
import asyncio
import random
import datetime


STATE_IDLE = "IDLE"
STATE_ASSESS = "ASSESS"
STATE_RESPOND = "RESPOND"


class RescueAgent(Agent):


    class IdleState(State):
        async def run(self):
            print("\nState: IDLE - Waiting for disaster event...")
            await asyncio.sleep(2)
            self.set_next_state(STATE_ASSESS)

    
    class AssessState(State):
        async def run(self):
            print("\nState: ASSESSING EVENT")

            
            severity = random.randint(1, 5)
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            print(f"[{timestamp}] Detected disaster severity level: {severity}")

            
            self.agent.severity = severity

            
            if severity >= 4:
                print("High severity detected! Initiating rescue response.")
                self.set_next_state(STATE_RESPOND)
            else:
                print("Low severity. Returning to idle.")
                self.set_next_state(STATE_IDLE)

    
    class RespondState(State):
        async def run(self):
            print("\nState: RESPONDING TO DISASTER")
            await asyncio.sleep(3)
            print("Rescue mission completed successfully.")
            self.set_next_state(STATE_IDLE)

    
    async def setup(self):
        print(f"{self.name} started.")

        fsm = FSMBehaviour()

        # Add states
        fsm.add_state(name=STATE_IDLE, state=self.IdleState(), initial=True)
        fsm.add_state(name=STATE_ASSESS, state=self.AssessState())
        fsm.add_state(name=STATE_RESPOND, state=self.RespondState())

        
        fsm.add_transition(source=STATE_IDLE, dest=STATE_ASSESS)
        fsm.add_transition(source=STATE_ASSESS, dest=STATE_RESPOND)
        fsm.add_transition(source=STATE_ASSESS, dest=STATE_IDLE)
        fsm.add_transition(source=STATE_RESPOND, dest=STATE_IDLE)

        self.add_behaviour(fsm)



async def main():
    agent = RescueAgent("sensoragent2005@xmpp.jp", "Ilovechrist123")
    await agent.start()

    
    await asyncio.sleep(30)

    await agent.stop()


if __name__ == "__main__":
    asyncio.run(main())
