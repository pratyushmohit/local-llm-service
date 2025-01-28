import json
import logging

import tornado.ioloop
import tornado.web
import tornado.websocket

from agent.agent import stream_agent_updates

# Configure logging to print to the console with a professional format
logging.basicConfig(
    level=logging.INFO,  # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format="%(levelname)s: %(asctime)s - %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"  # Use a professional date format
)


class AgentHandler(tornado.websocket.WebSocketHandler):
    async def on_message(self, message):
        """
        Handle incoming WebSocket messages from clients.
        Stream responses as they are generated.
        """
        try:
            # Parse the incoming message
            user_message = json.loads(message).get("content")
            if not user_message:
                self.write_message(json.dumps({
                    "error": "Invalid message format. Expected {'content': '<user_message>'}."
                }))
                return

            logging.info(f"Received message from user: {user_message}")

            # Stream response back to the client
            async for response in stream_agent_updates(user_message):
                logging.info(f"Response: {response}")
                self.write_message(json.dumps(response))

        except Exception as e:
            logging.error(f"Error occurred: {e}", exc_info=True)  # Log error with traceback
            self.write_message(json.dumps({
                "error": "An unexpected error occurred. Please try again later."
            }))

    def check_origin(self, origin):
        """
        Allow CORS for development. Restrict in production!
        """
        return True  # Change to `origin in allowed_origins` for production

    def on_close(self):
        """
        Handle WebSocket disconnection if needed.
        """
        logging.info("WebSocket connection closed")


if __name__ == "__main__":
    try:
        app = tornado.web.Application([(r"/chat", AgentHandler)])
        app.listen(8888)  # Service will run on localhost:8888
        logging.info("Tornado server is running at ws://localhost:8888/chat")
        tornado.ioloop.IOLoop.current().start()
        
    except KeyboardInterrupt:
        logging.info("Shutting down Tornado server.")
        tornado.ioloop.IOLoop.current().stop()
