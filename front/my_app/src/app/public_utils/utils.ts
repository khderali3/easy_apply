 

export const getErrorMessage = (errorData:any) => {

  if (errorData?.data) {
    errorData = errorData.data;
  }

  if (!errorData) return "An error occurred"; 

  if (typeof errorData === "string") {
    return errorData;  
  }

  if (Array.isArray(errorData)) {
    return errorData.join(", "); 
  }

  if (typeof errorData === "object") {
   
    if ("message" in errorData) {
      return errorData.message;
    }
    if ("detail" in errorData) {
      return errorData.detail;
    }

    return Object.entries(errorData)
      .map(([key, value]) => `${key}: ${Array.isArray(value) ? value.join(", ") : value}`)
      .join(" | ");
  }

  return "An unexpected error occurred";  
};


 