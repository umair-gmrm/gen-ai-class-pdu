import streamlit as st
from agent import get_agent_response


def get_response(message:str):
    prev_messages = st.session_state.get("messages", [])
    response = get_agent_response(message , prev_messages )

    return {
        "user": message,
        "agent": response["agent"]
    }


def main():
    st.title("Travel Support Agent")


    message = st.chat_input("Ask your travel-related questions here...")
    messages = st.session_state.get("messages", [])


    if message:
        response = get_response(message)
        messages.append({"user": message, "agent": response["agent"]})
        st.session_state["messages"] = messages


    if messages:
        for msg in messages:
            st.write("User :", msg["user"])
            st.write("Agent :", msg["agent"])
     

    


if __name__ == "__main__":
    main()