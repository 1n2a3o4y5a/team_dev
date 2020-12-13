FROM node

WORKDIR /app
COPY ./package.json /app/package.json
RUN npm install -g @vue/cli
RUN npm install
COPY . .
RUN npm run build
RUN npm run serve
EXPOSE 8080
