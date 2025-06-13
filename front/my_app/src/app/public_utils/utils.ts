

export const getErrorMessage = (errorData:any) => {

  if (errorData?.data) {
    errorData = errorData.data;
  }


  if (!errorData) return "An error occurred"; // Default message if data is empty

  if (typeof errorData === "string") {
    return errorData; // Return the string directly
  }

  if (Array.isArray(errorData)) {
    return errorData.join(", "); // Convert list to a single message
  }

  if (typeof errorData === "object") {
    // If errorData is an object, return key-value pairs



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

  return "An unexpected error occurred"; // Fallback message
};


 