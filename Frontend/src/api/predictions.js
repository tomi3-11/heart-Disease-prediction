import api from "./client";

export async function createPrediction(patientId) {
    const response = await api.post("/predictions/", {
        patient_id: patientId,
    });

    return response.data;
}

export async function getPredictionHistory() {
    const response = await api.get("/predictions/");
    return response.data;
}
