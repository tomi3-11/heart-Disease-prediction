# Heart Disease Predictor - Frontend UI

This is the React frontend for the Heart Disease Prediction assignment. 

## Running the Application
Ensure you have Node.js installed, then run:

```bash
npm install
npm run dev
```

The application will be accessible at `http://localhost:5173`.

---

## 🚀 Backend Integration Guide (For the Backend Developer)

To the backend developer: The UI is completely built and ready to be connected to your Machine Learning Node.js service.

Here are the integration points you need to wire up:

### 1. Prediction Endpoint (Machine Learning Model)
**File to edit:** `src/App.jsx` -> `handlePrediction` function

**Expected Request Body:**
The form collects and submits the following JSON structure. You should map this to your ML model's features:
```json
{
  "Age": 50,
  "Sex": 1,
  "ChestPainType": 0,
  "RestingBP": 130,
  "Cholesterol": 200,
  "FastingBS": 0,
  "RestingECG": 0,
  "MaxHR": 150,
  "ExerciseAngina": 0,
  "Oldpeak": 0.0,
  "ST_Slope": 1
}
```

**Expected Response Body:**
The frontend expects a response in this format:
```json
{
  "prediction": 1, 
  "probability": 0.85
}
```
*Note: `prediction: 1` triggers the "HIGH RISK" UI state, while `prediction: 0` triggers "NOMINAL".*

### 2. Authentication Endpoint (Optional)
**File to edit:** `src/components/AuthModal.jsx` -> `onSubmit` handler
If you are implementing user authentication, you will need to add fetch calls in the `AuthModal` component to handle login/signup endpoints. Currently, it just prevents the default form submission.

### Environment Variables
Consider adding a `.env` file (e.g., `VITE_API_BASE_URL=http://localhost:3000`) and replacing the simulated `setTimeout` logic in `App.jsx` with actual `fetch` or `axios` calls pointing to your Node.js server.
