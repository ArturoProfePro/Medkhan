export interface CheckUp {
  id: number;
  name: string;
  description: string;
  originalPrice: number;
  discountedPrice: number;
  gender: string;
  CheckUpType: string;
  expiredAt: string;
  discountPercentage: number;
}
export interface CheckUpResponse {
  data: CheckUp[];
  pagination: {
    total: number;
  };
}
