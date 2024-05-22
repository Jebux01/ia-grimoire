FROM node:14 as build

WORKDIR /app

COPY package.json ./
COPY package-lock.json ./
RUN npm install
COPY . ./

EXPOSE 3000
CMD ["nginx", "-g", "daemon off;"]
