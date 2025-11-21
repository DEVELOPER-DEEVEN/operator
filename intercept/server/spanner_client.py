from google.cloud import spanner
import datetime
import os

class SpannerClient:
    def __init__(self, instance_id="intercept-instance", database_id="intercept-db"):
        self.project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")
        self.instance_id = instance_id
        self.database_id = database_id
        self.client = None
        self.instance = None
        self.database = None
        self._connect()

    def _connect(self):
        if not self.project_id:
            print("Warning: GOOGLE_CLOUD_PROJECT not set. Spanner disabled.")
            return

        try:
            self.client = spanner.Client(project=self.project_id)
            self.instance = self.client.instance(self.instance_id)
            self.database = self.instance.database(self.database_id)
        except Exception as e:
            print(f"Failed to connect to Spanner: {e}")

    def log_transaction(self, session_id, action, status):
        if not self.database:
            return

        def _insert_transaction(transaction):
            transaction.insert(
                "Transactions",
                columns=["TransactionId", "SessionId", "Action", "Status", "Timestamp"],
                values=[
                    (
                        spanner.COMMIT_TIMESTAMP, # Using commit timestamp as ID for simplicity in this demo, ideally UUID
                        session_id,
                        str(action),
                        status,
                        spanner.COMMIT_TIMESTAMP
                    )
                ],
            )

        try:
            self.database.run_in_transaction(_insert_transaction)
        except Exception as e:
            print(f"Spanner transaction failed: {e}")
