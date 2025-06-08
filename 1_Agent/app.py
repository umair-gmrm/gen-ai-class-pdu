import streamlit as st


def get_response(message:str):

    return {
        "user": message,
        "agent": "This is a placeholder response. I can provide information on travel destinations, tips, and more. How can I assist you today?"
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