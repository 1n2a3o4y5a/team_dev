FROM node

WORKDIR /app
COPY ./package.json /app/package.json
RUN npm install -g @vue/cli
RUN npm install
RUN npm install --save @vue/cli-service
COPY . .

CMD [ "npm", "run", "build" ]

CMD [ "npm", "run", "serve" ]