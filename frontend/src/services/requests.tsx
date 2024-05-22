import { client } from "../api";

export interface HTTPResponse {
  status: number;
  detail?: any;
  data?: any;
  response?: any;
  request?: any;
}

export const get = async (url: string): Promise<HTTPResponse> => {
  return await client
    .get(url)
    .then((response) => {
      return response;
    })
    .catch((error) => {
      if (Array.isArray(error.response?.data?.detail)) {
        let msg = error.response.data.detail
          .map((element: any) => {
            return element.msg + " " + element.loc[1] + "\n";
          })
          .join("");

        error.response.data.detail = msg;
      }
      return { ...error };
    });
};

export const create = async (url: string, data: any): Promise<HTTPResponse> => {
  return await client
    .post(url, data)
    .then((response) => {
      return response;
    })
    .catch((error) => {
      if (Array.isArray(error.response?.data?.detail)) {
        let msg = error.response.data.detail
          .map((element: any) => {
            return element.msg + " " + element.loc[1] + "\n";
          })
          .join("");

        error.response.data.detail = msg;
      }
      return { ...error };
    });
};

export const put = async (url: string, data: any): Promise<HTTPResponse> => {
  return await client
    .put(url, data)
    .then((response) => {
      return response;
    })
    .catch((error) => {
      if (Array.isArray(error.response?.data?.detail)) {
        let msg = error.response.data.detail
          .map((element: any) => {
            return element.msg + " " + element.loc[1] + "\n";
          })
          .join("");

        error.response.data.detail = msg;
      }
      return { ...error };
    });
};

export const patch = async (url: string, data: any): Promise<HTTPResponse> => {
  return await client
    .patch(url, data, {
      headers: {
        "Content-Type": "application/json",
        accept: "application/json",
      },
    })
    .then((response) => {
      return response;
    })
    .catch((error) => {
      if (Array.isArray(error.response?.data?.detail)) {
        let msg = error.response.data.detail
          .map((element: any) => {
            return element.msg + " " + element.loc[1] + "\n";
          })
          .join("");

        error.response.data.detail = msg;
      }
      return { ...error };
    });
};

export const remove = async (url: string): Promise<HTTPResponse> => {
  return await client
    .delete(url)
    .then((response) => {
      return response;
    })
    .catch((error) => {
      if (Array.isArray(error.response?.data?.detail)) {
        let msg = error.response.data.detail
          .map((element: any) => {
            return element.msg + " " + element.loc[1] + "\n";
          })
          .join("");

        error.response.data.detail = msg;
      }
      return { ...error };
    });
};
