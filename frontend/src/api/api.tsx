import axios from 'axios';
import { DoctorResponse } from '../Interface/Doctor.interface';

export const fetchDoctors = async (): Promise<DoctorResponse> => {
  const res = await axios.get<DoctorResponse>(
    'http://localhost:8000/api/v1/doctors/'
  );
  return res.data;
};
