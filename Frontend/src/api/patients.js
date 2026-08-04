import api from "./client";

export async function createPatient(patient) {
    const response = await api.post("/patients/", patient);
    return response.data;
}

export async function getPatients() {
    const response = await api.get("/patients/");
    return response.data;
}

export async function getPatient(id) {
    const response = await api.get(`/patients/${id}`);
    return response.data;
}

export async function deletePatient(id) {
    await api.delete(`/patients/${id}`);
}
