
---

### 6️⃣ `utils/consent_vault.py`  

```python
# Consent Vault module (simulation phase)
class ConsentVault:
    def __init__(self):
        self.consent = {}

    def grant_consent(self, user_id):
        self.consent[user_id] = True

    def revoke_consent(self, user_id):
        self.consent[user_id] = False

    def check_consent(self, user_id):
        return self.consent.get(user_id, False)
      
