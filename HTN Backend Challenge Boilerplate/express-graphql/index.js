import express from "express";
import { graphqlHTTP } from "express-graphql";
import sqlite3 from "sqlite3";
import graphql from "graphql";

const port = process.env.PORT || 3000;

const app = express();

// Create a database if none exists
const database = new sqlite3.Database("hackers.db");

const queryType = new graphql.GraphQLObjectType({
  name: "Query",
  fields: {
    hello: {
      type: graphql.GraphQLString,
      resolve: (root, args, context, info) => {
        return "Hello, World!";
      },
    },
  },
});

const schema = new graphql.GraphQLSchema({
  query: queryType,
});

app.use("/", graphqlHTTP({ schema: schema, graphiql: true }));

app.listen(port, () => {
  console.log(`GraphQL server running at http://localhost:${port}`);
});
