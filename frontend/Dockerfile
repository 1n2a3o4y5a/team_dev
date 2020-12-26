FROM node

WORKDIR /app
COPY ./package.json /app/package.json
RUN npm install -g @vue/cli
RUN npm install
COPY . .

CMD [ "npm", "run", "build" ]

CMD [ "npm", "run", "serve" ]