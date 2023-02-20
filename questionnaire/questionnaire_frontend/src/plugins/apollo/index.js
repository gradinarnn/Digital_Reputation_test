import { createApolloProvider,  } from '@vue/apollo-option';

import { ApolloClient, InMemoryCache } from '@apollo/client/core'
import { HttpLink } from 'apollo-link-http'

const cache = new InMemoryCache()

const httpLink = new HttpLink({
 uri: 'http://192.168.31.100:5172/graphql/',
  credentials: "include"
})

const apolloClient = new ApolloClient({
  link: httpLink,
  cache: cache,
  connectToDevTools: true,
})


const apolloProvider = createApolloProvider({
  defaultClient: apolloClient,
})

export default apolloProvider;